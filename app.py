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
    """
    https://docs.synapsepay.com/docs/oauth-resources

    Resource: https://sandbox.synapsepay.com/api/3/oauth/:userid
    """
    return jsonify(**{
        "expires_at": "1443332477",
        "expires_in": "352259",
        "oauth_key": "iuda3QJXoILdGQKaAcfi67EkGjMgQKOkEnl6irWC",
        "refresh_token": "YGpR6tQmkPfkHJeLu8ixKtktDMqS96xs7A2qcuRi"
    })


@api.route('/users', methods=['GET', 'POST'])
def users():
    """
    https://docs.synapsepay.com/docs/user-resources

    Resource: https://sandbox.synapsepay.com/api/3/users
    """
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


@api.route('/users/<userid>', methods=['GET', 'PATCH'])
def get_user(userid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id
    """
    return_data = jsonify(**{
        "_id": "557387ed86c27318532fc09a",
        "_links": {
            "self": {
                "href": "https://sandbox.synapsepay.com/api/3/users/557387ed86c27318532fc09a"
            }
        },
        "client": {
            "id": 844,
            "name": "SynapsePay*Sandbox"
        },
        "extra": {
            "date_joined": 1436739787426,
            "is_business": False,
            "supp_id": "122eddfgbeafrfvbbb"
        },
        "is_hidden": False,
        "legal_names": [
            "Test User",
            "Some new name"
        ],
        "logins": [{
            "email": "test1@synapsepay.com",
            "read_only": False
        }],
        "permission": "SEND-AND-RECEIVE",
        "phone_numbers": [
            "901.942.8167"
        ],
        "photos": [
            "https://synapse_django.s3.amazonaws.com/sandbox_attachments/2015/09/02/fcf495a0-3ba1-4947-bdcf-b1df9830d9da.png"
        ],
        "refresh_token": "YGpR6tQmkPfkHJeLu8ixKtktDMqS96xs7A2qcuRi"
    })
    if request.method == 'GET':
        print("Requested for user")
        return return_data
    elif request.method == 'PATCH':
        data = request.get_json()
        if 'doc' in data:
            if 'attachments' in data['doc']:
                print("Passed Attachment")
            elif 'question_set_id' in data['doc']:
                print("Passed Question set")
            else:
                print("Passed Virtual Document")
        else:
            print("Update User")
        return return_data
    else:
        return 'Error'


app.register_blueprint(api, url_prefix='/api/3')


@app.route('/')
def index():
    return 'Follow synapse api docs'


if __name__ == '__main__':
    app.run(debug=True)
