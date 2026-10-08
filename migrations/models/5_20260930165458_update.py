from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "taskrun" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "deleted_at" TIMESTAMPTZ,
    "run_id" VARCHAR(32) NOT NULL UNIQUE,
    "user_id" BIGINT,
    "task_id" VARCHAR(32) NOT NULL,
    "rules" JSONB NOT NULL,
    "status" VARCHAR(32) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "taskrun";"""


MODELS_STATE = (
    "eJztml9v2jAQwL9K5KdOYhUNpXS80a5bOw2Y2mibOk2WSQxkJDaznbVdx3ef7CTkL5Swrg"
    "Xqt3DnI87vfL7zJffApw72+H4X8cll4GHQNu4BQb68KOhqBkDTaaKRAoEGygr4iE9YPGrA"
    "BUO2AG1jiDyOawZwMLeZOxUuJaBtkMDzpJDaXDCXjBJRQNyfAYaCjrAYYwbaxrfvNQO4xM"
    "G3mMc/pxM4dLHnZKbrOvLeSg7F3VTJLoh4pwbKuw2gTb3AJ8ng6Z0YUzIf7RIhpSNMMEMC"
    "y78XLJDTl7OLnjR+onCmyZBwiikbBw9R4InU4w5gIgMQ9voWvDqzIAQVANmUSLguEZLGPR"
    "jJKbw2Dw5bh8eNo8PjmgHUNOeS1iy8dQImNFR4ehaYKT0SKByhGCdQbYYlCYhEEe5bJLBw"
    "fVxOOGuZI+1EpvvxRZ57THkZ+FiQkE9W21OgZxg5feLdRS5fwtm66J5dWZ3uJ3k7n/Ofnu"
    "LXsc6kxlTSu5x07+iVlFOG7DDC5n9ifLmwzg3507ju984UXsrFiKk7JuOsayDnhAJBIaE3"
    "EDmp1RlLY2qzWiqUgqmzptezltrrm+L1mFHK7dHsE6872MPreT1r+Qhejxbppjh9e51cjG"
    "2B+ASW5crTMWLl7k2Z5HzLBVsnhp83ZfroFnqYjMQYtI2GucS5nzuXp+edy72GmXNYL9KY"
    "SjXLAJZVEC/i/XDV75XjnRvkA8e1hfHH8FwutnCjXIJVosiES4xzr9v5mid9+rF/ko8D+Q"
    "cnYDaTteAwqgXnxeEA2ZMbxBxY0FCTLhpbVPmmn5cggkYKpHxi+XxRhWwhPimrnJV8adUs"
    "I0tXzLpi1hXzBqdVXTG/RK/rillXzFFsc8xKK+YTd7QwXaaMHs6Zm+/PKGu+Mc1Go2XWG0"
    "fHzcNWq3lcn6fPompZHj25eC9TacancW7VZ5UnO6sMXQ+r6wqE0zaPg/i513YGstlsrkDZ"
    "bDYXYla6IueQUkXQc6NdJF1fBXR9Med6KWbu/sbV9uqM2Vq79caBfpbtmtOA2RjSwQ9siy"
    "orvWC4g6u9WV9luTfri9e70uUSJBXIg4ze8GorPmunC5S1CxTFMeRa4oIH+KfsdsgF/9hZ"
    "SW0nAomAV9pH5hZPt4HEbRuwRSXgBvVNLwOyqHUqVQ92T1k0SDdQtyvMdQP15bTSdAP1JX"
    "pdN1B1AzV+I04qdvESC93Ee7CJp/vTL7k//dzg9dc0u/I1zRaevVlAiMS2RYt7Q87eHcxc"
    "e1x29I40S0/eKBmjD967cvD+hRmXU6oQ9CmTHcxm/+VVoAyqCoSj4TtI92ClFyIHS16IKF"
    "2Wrk2JwGFor1owpEx0ydDdog9wZ38Bb5hcjA=="
)
