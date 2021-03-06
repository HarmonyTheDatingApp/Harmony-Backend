from flask_restful import Resource
from flask import Flask, request, jsonify, make_response

from harmony.models.user import UserAccount, UserPreference, SexualOrientation
from harmony.resources.auth import token_required
from harmony import db


class UserSettings(Resource):
    # method_decorators = [token_required]

    def get(self):
        request_data = request.args
        if not 'user_id' in request_data:
            return make_response(jsonify({'message': "No user id given", 'success': False}), 400)
        user = UserAccount.query.filter_by(public_id=request_data['user_id']).first()
        if not user:
            return make_response(jsonify({'message': "Wrong user id given", 'success': False}), 404)
        print(user.preference_id)
        if user.preference_id:
            preference = UserPreference.query.get(user.preference_id)
            if not preference:
                return make_response(jsonify({'message': "Wrong Preference ID", 'success': False}), 400)
        else:
            preference = None
        if user.sexual_orientation_id:
            sexual_orientation = SexualOrientation.query.get(user.sexual_orientation_id)
            if not sexual_orientation:
                return make_response(jsonify({'message': "Wrong Preference ID", 'success': False}), 400)
        else:
            sexual_orientation = None
        sexual_orientation_list = SexualOrientation.query.all()
        sexual_orientations = []
        for orientation in sexual_orientation_list:
            sexual_orientations.append({'name': orientation.name, 'id': orientation.id})
        print(preference)
        data = {
            'name': user.f_name,
            'bio': user.bio,
            'job': user.job,
            'gender': user.gender,
            'birth_date': user.birth_date,
            'age_min': preference.age_min if preference else None,
            'age_max': preference.age_max if preference else None,
            'interested_gender': preference.interested_gender if preference else None,
            'sexual_orientation_name': sexual_orientation.name if sexual_orientation else None,
            'sexual_orientation_id': sexual_orientation.id if sexual_orientation else None,
            'sexual_orientation_list': sexual_orientations,
            'ytmusic_link': user.ytmusic_link,
            'spotify_link': user.spotify_link
        }
        return make_response(jsonify({'success': True, 'data': data}), 200)

    def post(self):

        request_data = request.get_json()
        if not 'user_id' in request_data:
            return make_response(jsonify({'message': "No user id given", 'success': False}), 400)
        user = UserAccount.query.filter_by(public_id=request_data['user_id']).first()
        if not user:
            return jsonify({'message': "Wrong user id given", 'success': False}), 404
        if 'name' in request_data:
            user.f_name = request_data['name']
        if 'bio' in request_data:
            user.bio = request_data['bio']
        if 'gender' in request_data:
            user.gender = request_data['gender']
        if 'job' in request_data:
            user.job = request_data['job']
        if 'birth_date' in request_data:
            user.birth_date = request_data['birth_date']
        preference = UserPreference.query.filter_by(user_id=user.id).first()
        print(preference)
        print(user)
        if not preference:
            print("creating preference")
            preference = UserPreference(user_id=user.id)
            db.session.add(preference)
            db.session.commit()
            print(preference.id)
            user.preference_id = preference.id
            print(user.preference_id)
        print(user.preference_id)
        if 'age_min' in request_data:
            preference.age_min = request_data['age_min']
        if 'age_max' in request_data:
            preference.age_max = request_data['age_max']
        if 'interested_gender' in request_data:
            preference.interested_gender = request_data['interested_gender']
            print(request_data['interested_gender'])
        if 'sexual_orientation_id' in request_data:
            user.sexual_orientation_id = request_data['sexual_orientation_id']
        if 'ytmusic_link' in request_data:
            user.ytmusic_link = request_data['gender']
        if 'spotify_link' in request_data:
            user.spotify_link = request_data['spotify_link']
        db.session.add(user)
        db.session.commit()
        db.session.add(preference)
        db.session.commit()
        print(user.preference_id)
        return make_response(jsonify({'success': True}), 200)
