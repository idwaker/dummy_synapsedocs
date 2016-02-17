#! -*- coding: utf-8 -*-
"""
Dummy API Service for synapsepay, from docs

See: https://docs.synapsepay.com/docs/
"""

import os
from os.path import join as pjoin
from flask import Flask, Blueprint, request, jsonify


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
api = Blueprint('api', __name__)
app = Flask(__name__)
RESULT_DIR = pjoin(BASE_DIR, 'results')



@api.route('/oauth/<userid>', methods=['POST'])
def oauth_user(userid):
    """
    https://docs.synapsepay.com/docs/oauth-resources

    Resource: https://sandbox.synapsepay.com/api/3/oauth/:userid
    """
    return open(pjoin(RESULT_DIR, 'oauth.json'), 'r').read()


@api.route('/users', methods=['GET', 'POST'])
def users():
    """
    https://docs.synapsepay.com/docs/user-resources

    Resource: https://sandbox.synapsepay.com/api/3/users
    """
    if request.method == 'GET':
        return open(pjoin(RESULT_DIR, 'users-get.json')).read()
    else:
        return open(pjoin(RESULT_DIR, 'users-post.json')).read()


@api.route('/users/<userid>', methods=['GET', 'PATCH'])
def get_user(userid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id
    """
    result = open(pjoin(RESULT_DIR, 'user-get.json')).read()
    if request.method == 'GET':
        print("Requested for user")
        return result
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
        return result
    else:
        raise Exception("Unknown request method")


@api.route('/users/<userid>/nodes', methods=['GET', 'POST'])
def user_nodes(userid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id/nodes
    """
    if request.method == 'GET':
        return open(pjoin(RESULT_DIR, 'nodes-get.json')).read()
    else:
        data = request.get_json()
        if 'type' in data:
            if data['type'] == 'SYNAPSE-US':
                return open(pjoin(RESULT_DIR, 'node-post-synapse-us.json')).read()
            elif data['type'] == 'ACH-US':
                if 'routing_num' in data['info']:
                    return open(pjoin(RESULT_DIR, 'node-post-ach-acrt.json')).read()
                else:
                    return open(pjoin(RESULT_DIR, 'node-post-ach-us.json')).read()
            elif data['type'] == 'WIRE-US':
                return open(pjoin(RESULT_DIR, 'node-post-wire-us.json')).read()
            elif data['type'] == 'WIRE-INT':
                return open(pjoin(RESULT_DIR, 'node-post-wire-int.json')).read()
            elif data['type'] == 'IOU':
                return open(pjoin(RESULT_DIR, 'node-post-iou.json')).read()
            else:
                raise Exception("Unknown Type")
        if 'mfa_answer' in data:
            return open(pjoin(RESULT_DIR, 'node-post-ach-mfa.json')).read()
        else:
            raise Exception("Type not defined")


@api.route('/users/<userid>/node/<nodeid>', methods=['GET', 'PATCH', 'DELETE'])
def user_node(userid, nodeid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id/nodes/:node_id
    """
    if request.method == 'GET':
        return open(pjoin(RESULT_DIR, 'user-node-get.json')).read()
    elif request.method == 'PATCH':
        return open(pjoin(RESULT_DIR, 'user-node-patch.json')).read()
    elif request.method == 'DELETE':
        return open(pjoin(RESULT_DIR, 'user-node-delete.json')).read()
    else:
        raise Exception("Unknown Method")


@api.route('/users/<userid>/nodes/<nodeid>/trans', methods=['GET', 'POST'])
def transaction(userid, nodeid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id/nodes/:node_id/trans
    """
    if request.method == 'GET':
        return open(pjoin(RESULT_DIR, 'trans-get.json')).read()
    else:
        return open(pjoin(RESULT_DIR, 'trans-post.json')).read()


@api.route('/users/<userid>/nodes/<nodeid>/trans/<transid>',
           methods=['GET', 'PATCH', 'DELETE'])
def user_transaction(userid, nodeid, transid):
    """
    https://sandbox.synapsepay.com/api/3/users/:user_id/nodes/:node_id/trans/:trans_id
    """
    if request.method == 'GET':
        return open(pjoin(RESULT_DIR, 'user-trans-get.json')).read()
    elif request.method == 'PATCH':
        return open(pjoin(RESULT_DIR, 'user-trans-patch.json')).read()
    elif request.method == 'DELETE':
        return open(pjoin(RESULT_DIR, 'user-trans-delete.json')).read()
    else:
        raise Exception("Unknown Method")


app.register_blueprint(api, url_prefix='/api/3')


@app.route('/')
def index():
    return 'Follow synapse api docs'


if __name__ == '__main__':
    app.run(debug=True)
