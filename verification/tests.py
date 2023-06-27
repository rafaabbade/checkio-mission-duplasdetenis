"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4]],
            "answer": 0
        },
        {
            "input": [[5,5,5,5]],
            "answer": 0
        },
        {
            "input": [[1,2,3,9]],
            "answer": 5
        }
    ],
    "Extra": [
        {
            "input": [[15,10,25,35]],
            "answer": 5
        },
    ]
}
