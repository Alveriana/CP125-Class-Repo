def is_bot(user_id, bot_ids):
    return user_id in bot_ids


def collect_user_actions(log_data, bot_ids):
    user_action = {}

    for timestamp, user_id, action_type in log_data:
        if not is_bot(user_id, bot_ids):
            if user_id not in user_action:
                user_action[user_id] = set()
            user_action[user_id].add(action_type)

    return user_action


def get_legit_power_users(log_data, bot_ids, threshold):
    user_action = collect_user_actions(log_data, bot_ids)

    power_users = []
    for user_id, actions in user_action.items():
        if len(actions) > threshold:
            power_users.append(user_id)

    return sorted(power_users)
