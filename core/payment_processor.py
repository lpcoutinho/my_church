import base64
import uuid
from io import BytesIO

import mercadopago
from PIL import Image


class PaymentProcessor:
    def __init__(self, access_token):
        self.sdk = mercadopago.SDK(access_token)
        self.sdk.advanced_payment

    def create_payment(self, email, amount=1, payment_method="pix", installments=1):
        # Geração de um UUID v4 para o cabeçalho de idempotência
        idempotency_key = str(uuid.uuid4())

        # Configuração das opções de requisição
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {"x-idempotency-key": idempotency_key}
        payment_method = payment_method.lower()

        # Dados do pagamento
        payment_data = {
            "installments": installments,
            "transaction_amount": amount,
            "payment_method_id": payment_method,
            "payer": {
                "email": email,
            },
        }
        # print('#'*5,'Dados do pagamento','#'*5,'\n',payment_data)

        # Criação do pagamento
        payment_response = self.sdk.payment().create(payment_data, request_options)
        payment = payment_response["response"]
        # print('#'*5,'Criação do pagamento','#'*5,'\n',payment)

        # Capturando as informações desejadas
        payment_info = {
            "date_created": payment.get("date_created"),
            "id": payment.get("id"),
            "last_updated": payment.get("last_updated"),
            "qr_code": payment.get("point_of_interaction", {})
            .get("transaction_data", {})
            .get("qr_code"),
            "qr_code_base64": payment.get("point_of_interaction", {})
            .get("transaction_data", {})
            .get("qr_code_base64"),
            "ticket_url": payment.get("point_of_interaction", {})
            .get("transaction_data", {})
            .get("ticket_url"),
        }

        return payment_info

    def save_qr_code_image(self, qr_code_base64, filename="qrcode/qr_code.png"):
        if qr_code_base64:
            qr_code_data = base64.b64decode(qr_code_base64)
            image = Image.open(BytesIO(qr_code_data))
            image.save(f"qrcode/{filename}.png")
            print(f"QR Code image saved as {filename}")
        else:
            print("No QR Code base64 data found.")
