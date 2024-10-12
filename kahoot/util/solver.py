from re import split
from base64 import b64decode
from py_mini_racer import MiniRacer

_evaluator: MiniRacer = MiniRacer()

def _do_xor(session_token: str, solution: str) -> str:
    decoded_token = b64decode(session_token).decode('utf-8', 'strict')
    sol_chars = [ord(s) for s in solution]
    sess_chars = [ord(s) for s in decoded_token]
    return "".join([chr(sess_chars[i] ^ sol_chars[i % len(sol_chars)]) for i in range(len(sess_chars))])

def solve_challenge(session_token: str, text: str) -> str:
    text = text.replace('\t', '', -1).encode('ascii', 'ignore').decode('utf-8')
    text = split("[{};]", text)
    replace_function = "return message.replace(/./g, function(char, position) {"
    rebuilt = [text[1] + "{", text[2] + ";", replace_function, text[7] + ";})};", text[0]]
    solution = _evaluator.eval("".join(rebuilt))
    return _do_xor(session_token, solution)
