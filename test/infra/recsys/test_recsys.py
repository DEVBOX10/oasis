'''测试recsys'''

from twitter.recsys import (rec_sys_personalized,
                            rec_sys_personalized_with_trace, rec_sys_random,
                            rec_sys_reddit)


def test_rec_sys_random_all_tweets():
    # 测试当推文数量小于等于最大推荐长度时的情况
    user_table = [{'user_id': 1}, {'user_id': 2}]
    tweet_table = [{'tweet_id': '1'}, {'tweet_id': '2'}]
    trace_table = []
    rec_matrix = [[None], [], []]
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    expected = [None, ['1', '2'], ['1', '2']]
    result = rec_sys_random(user_table, tweet_table, trace_table, rec_matrix,
                            max_rec_tweet_len)
    assert result == expected


def test_rec_sys_reddit_all_tweets():
    # 测试当推文数量小于等于最大推荐长度时的情况
    tweet_table = [{'tweet_id': '1'}, {'tweet_id': '2'}]
    rec_matrix = [[None], [], []]
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    expected = [None, ['1', '2'], ['1', '2']]
    result = rec_sys_reddit(tweet_table, rec_matrix, max_rec_tweet_len)
    assert result == expected


def test_rec_sys_personalized_all_tweets():
    # 测试当推文数量小于等于最大推荐长度时的情况
    user_table = [{
        'user_id': 1,
        'bio': 'I like cats'
    }, {
        'user_id': 2,
        'bio': 'I like dogs'
    }]
    tweet_table = [{
        'tweet_id': '1',
        'user_id': 3,
        'content': 'I like dogs'
    }, {
        'tweet_id': '2',
        'user_id': 4,
        'content': 'I like cats'
    }]
    trace_table = []
    rec_matrix = [[None], [], []]
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    expected = [None, ['1', '2'], ['1', '2']]
    result = rec_sys_personalized(user_table, tweet_table, trace_table,
                                  rec_matrix, max_rec_tweet_len)
    assert result == expected


def test_rec_sys_personalized_with_trace_all_tweets():
    # 测试当推文数量小于等于最大推荐长度时的情况
    user_table = [{
        'user_id': 1,
        'bio': 'I like cats'
    }, {
        'user_id': 2,
        'bio': 'I like dogs'
    }]
    tweet_table = [{
        'tweet_id': '1',
        'user_id': 3,
        'content': 'I like dogs'
    }, {
        'tweet_id': '2',
        'user_id': 4,
        'content': 'I like cats'
    }]
    trace_table = []
    rec_matrix = [[None], [], []]
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    expected = [None, ['1', '2'], ['1', '2']]
    result = rec_sys_personalized_with_trace(user_table, tweet_table,
                                             trace_table, rec_matrix,
                                             max_rec_tweet_len)
    assert result == expected


def test_rec_sys_random_sample_tweets():
    # 测试当推文数量大于最大推荐长度时的情况
    user_table = [{'user_id': 1}, {'user_id': 2}]
    tweet_table = [{'tweet_id': '1'}, {'tweet_id': '2'}, {'tweet_id': '3'}]
    trace_table = []  # 在这个测试中未使用，但是为了完整性加入
    rec_matrix = [[None], [], []]  # 假设有两个用户
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    result = rec_sys_random(user_table, tweet_table, trace_table, rec_matrix,
                            max_rec_tweet_len)
    print(result)
    # 验证第一个元素是None
    assert result[0] is None
    # 验证每个用户获得了2个推文ID
    for rec in result[1:]:
        assert len(rec) == max_rec_tweet_len
        # 验证推荐的推文ID确实存在于原始推文ID列表中
        for tweet_id in rec:
            assert tweet_id in ['1', '2', '3']


def test_rec_sys_reddit_sample_tweets():
    # 测试当推文数量大于最大推荐长度时的情况
    tweet_table = [{
        'tweet_id': '1',
        'num_likes': 100000,
        'num_dislikes': 25,
        'created_at': "2024-06-25 12:00:00"
    }, {
        'tweet_id': '2',
        'num_likes': 90,
        'num_dislikes': 30,
        'created_at': "2024-06-26 12:00:00"
    }, {
        'tweet_id': '3',
        'num_likes': 75,
        'num_dislikes': 50,
        'created_at': "2024-06-27 12:00:00"
    }, {
        'tweet_id': '4',
        'num_likes': 70,
        'num_dislikes': 50,
        'created_at': "2024-06-27 13:00:00"
    }]
    rec_matrix = [[None], [], []]  # 假设有两个用户
    max_rec_tweet_len = 3  # 最大推荐长度设置为2

    result = rec_sys_reddit(tweet_table, rec_matrix, max_rec_tweet_len)
    print(result)
    # 验证每个用户获得了2个推文ID
    for rec in result[1:]:
        assert len(rec) == max_rec_tweet_len
        # 验证推荐的推文ID确实存在于原始推文ID列表中
        for tweet_id in rec:
            assert tweet_id in ['3', '4', '1']


def test_rec_sys_personalized_sample_tweets():
    # 测试当推文数量大于最大推荐长度时的情况
    user_table = [{
        'user_id': 1,
        'bio': 'I like cats'
    }, {
        'user_id': 2,
        'bio': 'I like dogs'
    }]
    tweet_table = [{
        'tweet_id': '1',
        'user_id': 3,
        'content': 'I like dogs'
    }, {
        'tweet_id': '2',
        'user_id': 4,
        'content': 'I like cats'
    }, {
        'tweet_id': '3',
        'user_id': 5,
        'content': 'I like birds'
    }]
    trace_table = []  # 在这个测试中未使用，但是为了完整性加入
    rec_matrix = [[None], [], []]  # 假设有两个用户
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    result = rec_sys_personalized(user_table, tweet_table, trace_table,
                                  rec_matrix, max_rec_tweet_len)
    print(result)
    # 验证第一个元素是None
    assert result[0] is None
    # 验证每个用户获得了2个推文ID
    for rec in result[1:]:
        assert len(rec) == max_rec_tweet_len
        # 验证推荐的推文ID确实存在于原始推文ID列表中
        for tweet_id in rec:
            assert tweet_id in ['1', '2', '3']

    # personalized 推荐应该是根据用户的bio进行推荐
    for i in range(1, len(result)):
        if i == 1:
            assert result[i] == ['2', '1']

        if i == 2:
            assert result[i] == ['1', '2']


def test_rec_sys_personalized_with_trace_sample_tweets():
    # 测试当推文数量大于最大推荐长度时的情况
    user_table = [{
        'user_id': 1,
        'bio': 'I like cats'
    }, {
        'user_id': 2,
        'bio': 'I like dogs'
    }]
    tweet_table = [{
        'tweet_id': '1',
        'user_id': 3,
        'content': 'I like dogs'
    }, {
        'tweet_id': '2',
        'user_id': 4,
        'content': 'I like cats'
    }, {
        'tweet_id': '3',
        'user_id': 5,
        'content': 'I like birds'
    }]
    trace_table = [{
        'user_id': 1,
        'tweet_id': '3',
        'action': 'like'
    }, {
        'user_id': 2,
        'tweet_id': '2',
        'action': 'like'
    }]
    rec_matrix = [[None], [], []]  # 假设有两个用户
    max_rec_tweet_len = 2  # 最大推荐长度设置为2

    result = rec_sys_personalized_with_trace(user_table, tweet_table,
                                             trace_table, rec_matrix,
                                             max_rec_tweet_len)

    print(result)
    # 验证第一个元素是None
    assert result[0] is None

    # 验证每个用户获得了2个推文ID
    for rec in result[1:]:
        assert len(rec) == max_rec_tweet_len
        # 验证推荐的推文ID确实存在于原始推文ID列表中
        for tweet_id in rec:
            assert tweet_id in ['1', '2', '3']

    # personalized 推荐应该是根据用户的bio进行推荐
