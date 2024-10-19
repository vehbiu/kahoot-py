from base64 import b64decode

def _do_xor(session_token: str, solution: str) -> str:
    decoded_token = b64decode(session_token).decode('utf-8', 'strict')
    sol_chars = [ord(s) for s in solution]
    sess_chars = [ord(s) for s in decoded_token]
    return "".join([chr(sess_chars[i] ^ sol_chars[i % len(sol_chars)]) for i in range(len(sess_chars))])

def decode(offset: int, message):
    decoded_message = ''
    
    for position, char in enumerate(message):
        decoded_char = chr((((ord(char) * position) + offset) % 77) + 48)
        decoded_message += decoded_char
    
    return decoded_message

def solve_challenge(session_token: str, text: str) -> str:
    text = text.replace('\t', '', -1).encode('ascii', 'ignore').decode('utf-8')
    offset: int = int(eval(text.split("offset = ")[1].split(";")[0]))
    input = text.split("this, '")[1].split("'")[0]
    solution = decode(offset, input)
    return _do_xor(session_token, solution)
