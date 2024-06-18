from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/.well-known/assetlinks.json')
def get_asset_links():
    return send_from_directory('.well-known', 'assetlinks.json')
