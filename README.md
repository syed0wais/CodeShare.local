# Local Codeshare

A simple **local network code sharing tool** built with **Flask + Monaco Editor**.
Paste code on one device, open the same URL on another (same WiFi), and share instantly.

---

## 🚀 How to Run

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/local-codeshare.git](https://github.com/yourusername/local-codeshare.git)
    cd local-codeshare
    ```

2.  **Install dependencies**
    ```bash
    pip install flask
    ```

3.  **Run the server**
    ```bash
    python app.py
    ```

4.  **Open in your browser**
    * **On your main device:** `http://localhost:5000`
    * **On another device (same WiFi):** `http://<your-ip>:5000`

    *(You can find your IP address using `ipconfig` on Windows or `ifconfig` on macOS/Linux.)*
