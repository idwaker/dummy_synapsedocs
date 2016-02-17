#! -*- coding: utf-8 -*-
"""
Dummy API Service for synapsepay, from docs

See: https://docs.synapsepay.com/docs/
"""

from flask import Flask, Blueprint, request, jsonify


api = Blueprint('api', __name__)
app = Flask(__name__)


@api.route('/oauth/<userid>', methods=['POST'])
def oauth_user(userid):
    return jsonify(**{
        "expires_at": "1443332477",
        "expires_in": "352259",
        "oauth_key": "iuda3QJXoILdGQKaAcfi67EkGjMgQKOkEnl6irWC",
        "refresh_token": "YGpR6tQmkPfkHJeLu8ixKtktDMqS96xs7A2qcuRi"
    })


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify(**{
            "error_code": "0",
            "http_code": "200",
            "page": 1,
            "page_count": 1,
            "success": True,
            "users": [{
                "_id": "55aff52586c2732ee1633f90",
                "_links": {
                    "self": {
                        "href": "https://sandbox.synapsepay.com/api/3/users/55aff52586c2732ee1633f90"
                    }
                },
                "client": {
                    "id": 844,
                    "name": "SynapsePay*Sandbox"
                },
                "extra": {
                    "date_joined": 1437594917762,
                    "is_business": False,
                    "supp_id": ""
                },
                "is_hidden": False,
                "legal_names": [
                    "Sankaet Pathak"
                ],
                "logins": [{
                    "email": "sankaet@synapsepay.com",
                    "read_only": False
                }],
                "permission": "SEND-AND-RECEIVE",
                "phone_numbers": [
                    "9019428167"
                ],
                "photos": [],
                "refresh_token": "OTv4gQHCJ7l61JgoaE4w98eowOuxHdzWib85IefJ"
            }, ],
            "users_count": 3
        })
    else:
        return jsonify(**{
            "_id": "5602221886c2730550cc3716",
            "_links": {
                "self": {
                    "href": "https://sandbox.synapsepay.com/api/3/users/5602221886c2730550cc3716"
                }
            },
            "client": {
                "id": 844,
                "name": "SynapsePay*Sandbox"
            },
            "extra": {
                "date_joined": 1442980376688,
                "is_business": False,
                "supp_id": "122eddfgbeafrfvbbb"
            },
            "is_hidden": False,
            "legal_names": [
                "Test User"
            ],
            "logins": [{
                "email": "test1@synapsepay.com",
                "read_only": False
            }],
            "permission": "UNVERIFIED",
            "phone_numbers": [
                "901.111.1111"
            ],
            "photos": [],
            "refresh_token": "vVNAtuCon2bzjiLIAptjaKtgOoGwdYiKQVyiy414"
        })


app.register_blueprint(api, url_prefix='/api/3')


@app.route('/')
def index():
    return 'Follow synapse api docs'


if __name__ == '__main__':
    app.run(debug=True)
