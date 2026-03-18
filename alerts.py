from twilio.rest import Client
import streamlit as st


def send_alert(phone_number, risk, action):
    """
    Sends WhatsApp or SMS alert message for high-risk patients.
    Phone numbers must follow Twilio format:
        SMS: +233XXXXXXXXX
        WhatsApp: whatsapp:+233XXXXXXXXX
    """

    client = Client(
        st.secrets["twilio"]["account_sid"],
        st.secrets["twilio"]["auth_token"]
    )

    message_body = (
        f"⚠️ HIGH DEPRESSION RISK ALERT ⚠️\n"
        f"Risk Score: {risk:.3f}\n"
        f"Recommended Action: {action}\n"
        f"Immediate clinical attention is required."
    )

    message = client.messages.create(
        body=message_body,
        from_=st.secrets["twilio"]["from_number"],
        to=phone_number,
    )

    return message.sid
