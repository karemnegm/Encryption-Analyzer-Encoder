import tkinter as tk
from tkinter import ttk, messagebox
import base64, re, pyperclip, math, gzip, io
from PIL import Image, ImageTk


def base64_to_image(base64_str):
    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    return ImageTk.PhotoImage(image)

icon_base64 = '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'







def detect_encoding(ciphertext: str):
    result = []

    try:
        base64_bytes = base64.b64decode(ciphertext, validate=True)
        if base64_bytes:
            result.append("Base64")
    except Exception:
        pass

    try:
        bytes.fromhex(ciphertext)
        result.append("Hex")
    except ValueError:
        pass

    hash_lengths = {
        "MD5": 32,
        "SHA-1": 40,
        "SHA-224": 56,
        "SHA-256": 64,
        "SHA-384": 96,
        "SHA-512": 128,
    }

    for algo, length in hash_lengths.items():
        if len(ciphertext) == length and re.fullmatch(r'[a-fA-F0-9]+', ciphertext):
            result.append(f"Possible {algo} hash")

    if len(ciphertext) % 16 == 0:
        result.append("Possible AES")
    if len(ciphertext) % 8 == 0:
        result.append("Possible DES/3DES")

    if re.search(r'(.{4,8})\1{2,}', ciphertext):
        result.append("ECB pattern detected")


    entropy = calculate_entropy(ciphertext)
    result.append(f"Entropy: {entropy:.2f} bits/char")


    try:
        gzip.decompress(base64.b64decode(ciphertext))
        result.append("Contains GZIP compressed data")
    except:
        pass


    if is_simple_xor(ciphertext):
        result.append("Possible XOR-encrypted text")

    return result if result else ["Unknown or custom encryption"]

def calculate_entropy(data):
    if not data:
        return 0.0
    prob = [float(data.count(c)) / len(data) for c in set(data)]
    return -sum([p * math.log2(p) for p in prob])

def is_simple_xor(data):
    try:
        b = bytes.fromhex(data)
    except:
        try:
            b = base64.b64decode(data)
        except:
            return False

    for key in range(1, 256):
        try:
            decoded = bytes([x ^ key for x in b])
            if all(32 <= c <= 126 for c in decoded):  
                return True
        except:
            continue
    return False

def decrypt_cipher(ciphertext: str):
    try:
        decoded = base64.b64decode(ciphertext).decode('utf-8')
        return f"[Base64 Decoded]:\n{decoded}"
    except:
        pass

    try:
        decoded = bytes.fromhex(ciphertext).decode('utf-8')
        return f"[Hex Decoded]:\n{decoded}"
    except:
        pass

    try:
        decoded = gzip.decompress(base64.b64decode(ciphertext)).decode()
        return f"[GZIP + Base64 Decoded]:\n{decoded}"
    except:
        pass

    return "Unable to decode (Not Base64/Hex/GZIP)"

def analyze_input():
    text = input_text.get("1.0", tk.END).strip()
    result = detect_encoding(text)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(result))
    output_text.config(state="disabled")

def decode_input():
    text = input_text.get("1.0", tk.END).strip()
    decoded = decrypt_cipher(text)
    messagebox.showinfo("Decoded Output", decoded)

def copy_output():
    result = output_text.get("1.0", tk.END).strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No result to copy.")

##############################
root = tk.Tk()
root.title("Detect cipher type & analyzer")
root.geometry("760x600")
root.configure(bg="#0d0d0d")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="lime", background="black", font=("Courier", 12), padding=6)
style.configure("TLabel", background="#0d0d0d", foreground="lime", font=("Courier", 12))


root.iconphoto(False, base64_to_image(icon_base64))

ttk.Label(root, text="Enter Encrypted or Hashed Text:").pack(pady=10)

input_text = tk.Text(root, height=5, width=85, bg="#1c1c1c", fg="lime", insertbackground="white", font=("Courier", 10))
input_text.pack()

button_frame = tk.Frame(root, bg="#0d0d0d")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Analyze", command=analyze_input).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Try to Decrypt", command=decode_input).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="Copy Result", command=copy_output).grid(row=0, column=2, padx=10)

ttk.Label(root, text="📊 Analysis Result:").pack()
output_text = tk.Text(root, height=12, width=85, bg="#1c1c1c", fg="cyan", state="disabled", font=("Courier", 10))
output_text.pack(pady=10)


ttk.Label(root, text="Developer: Karim Mohamed", font=("Courier", 10, 'italic'), background="#0d0d0d", foreground="lime").pack(pady=10)

root.mainloop()
