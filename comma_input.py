# comma_input.py
from prompt_toolkit import PromptSession
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.document import Document

# Validator to ensure input is numeric and > 0
class NumberValidator(Validator):
    def validate(self, document: Document):
        text = document.text.replace(",", "")
        if not text.isdigit() or int(text) < 1:
            raise ValidationError(
                message="Enter a number greater than 0.",
                cursor_position=len(document.text)
            )

# Format a string of digits with commas
def format_number_with_commas(text: str) -> str:
    digits_only = text.replace(",", "")
    if digits_only == "":
        return ""
    return f"{int(digits_only):,}"

# Input number with live comma insertion
def input_number(message: str) -> int:
    session = PromptSession()

    # Attach live formatting to the session buffer using pre_run
    def pre_run():
        buf = session.default_buffer

        def on_change(event):
            text = buf.text
            digits_only = text.replace(",", "")
            if digits_only.isdigit() or digits_only == "":
                new_text = format_number_with_commas(text)
                if new_text != text:
                    buf.text = new_text
                    buf.cursor_position = len(new_text)

        buf.on_text_changed += on_change

    user_input = session.prompt(
        message,
        validator=NumberValidator(),
        validate_while_typing=True,
        pre_run=pre_run
    )
    return int(user_input.replace(",", ""))
