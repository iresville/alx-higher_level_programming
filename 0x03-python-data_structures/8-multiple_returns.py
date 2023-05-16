#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
    # return len(sentence), None

# def multiple_returns(sentence):
#     if not sentence:
#         return len(sentence), None
#     for i in sentence:
#         if isinstance(i, str):
#             return len(sentence), i
#     # return len(sentence), None
