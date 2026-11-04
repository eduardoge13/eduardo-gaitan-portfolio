"""Serve the portfolio and the same CV routes used by the production image."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
CV_ROUTES = {
    "/Eduardo_Gaitan_Resume_2026.pdf": "Eduardo_Gaitan_Resume_2026.pdf",
    "/Eduardo_Gaitan_CV_AI_Data_Scientist_2026.pdf":
        "Eduardo_Gaitan_CV_Airtm_AI_Data_Scientist_2026.pdf",
}


class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        resume = CV_ROUTES.get(urlsplit(path).path)
        if resume:
            return str(ROOT / "output" / "pdf" / resume)
        return super().translate_path(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8764)
    args = parser.parse_args()
    handler = partial(PreviewHandler, directory=str(ROOT))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Portfolio preview: http://127.0.0.1:{args.port}/", flush=True)
        server.serve_forever()
