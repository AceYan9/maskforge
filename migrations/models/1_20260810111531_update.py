from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "task" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "deleted_at" TIMESTAMPTZ,
    "user_id" BIGINT,
    "task_id" VARCHAR(32) NOT NULL,
    "filename" VARCHAR(255) NOT NULL,
    "file_type" VARCHAR(20) NOT NULL,
    "file_size" BIGINT NOT NULL,
    "source_object" VARCHAR(500) NOT NULL,
    "total_rows" BIGINT NOT NULL,
    "total_columns" INT NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "task";"""


MODELS_STATE = (
    "eJztmFtv2jAUgP9K5KdOYhUNpDDeoGMr0wpTG21Tp8kyiQleE5vZzlrW8d8nOwm5EChhl1"
    "LUt+Rc4uPvHOdY5x4EzMW+OLaRuAEd4x5QFGDQMXLymgHQbJZKlUCisa8NZWIxFpIjR4KO"
    "MUG+wDUDuFg4nMwkYRR0DBr6vhIyR0hOqJeKQkq+hxhK5mE5xRx0jC9fawYg1MV3WCSvsx"
    "s4Idh3c2ESV62t5VDOZ1o2oPKNNlSrjaHD/DCgqfFsLqeMLq0JlUrqYYo5klh9XvJQha+i"
    "i3eZ7CiKNDWJQsz4uHiCQl9mtjuGqQxAOBzZ8KpvQwgqAHIYVXAJlYrGPfBUCC/Nk2ar2W"
    "6cNts1A+gwl5LWIlo6BRM5ajxDGyy0HkkUWWjGKVSHY0UCIrkK9zWSWJIAlxPOexZIu7Hr"
    "cfJQ5J5Q3gQ+EaTk02r7H+g5Ru6I+vM45Rs424OL/pXdvfiglguE+O5rfl27rzSmls4L0q"
    "PTF0rOOHKi07X8iPFpYJ8b6tW4Hg37Gi8T0uN6xdTOvgYqJhRKBim7hcjNVGciTagtapmj"
    "FM7cHbOe93zO+r5kPWGUSXscfZp1F/t4t6znPf9C1uMi3ZekP90kl5xtgTks65U94q1tlx"
    "mnh3vm/ucz7pqvTLPRaJn1xmnbarZaVru+bJ+rqk19tDd4q1ppLqdJb03Jq+tRKfmzKeLl"
    "3DMuBe5C8qf49wzQHfQx9eQUdIyGuYHpx+7l2Xn38qhhFg7LMNaYWpVHPCE+1s8VGGd9Dh"
    "CyaVlbUDYtay1mrVvlHFGqCHrpdIik69uArq/nXC/FLMhPXO1vnXPb6X+9d6Af5YctWMgd"
    "DNn4G3ZklUpfcTzAarfq25S7VV9f71pXaJFMIh9ydiuqVXze77nkd7+jaJAR2JIcPJCAjN"
    "8h5eCPpitqXjWJ51XLAdYYOTe3iLtwRcNMts52VRWYQVGCKPI0KLUjFVw8vetiTpxp2Vwv"
    "1myc7KHU5nm2dyizvR+YCxVShcaWcTnAlvZPrsrqUFUgHJsfIN2TrS4MJxsuDFqXp+swKn"
    "F0tPOE312NhmsG06lLcVJFHGn8MnwinmKzWqyHq2Dk5lMJ06OL7uci7rP3o15x8KQ+0Hvs"
    "Zrb4DUajbdE="
)
