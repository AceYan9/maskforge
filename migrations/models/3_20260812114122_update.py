from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "task" ADD "status" VARCHAR(32) NOT NULL DEFAULT 'created';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "task" DROP COLUMN "status";"""


MODELS_STATE = (
    "eJztmFtv2jAUgP9K5KdOYhUNpDDeoGMr0wpTG21Tp8kyiQleg01tZy3r+O+TnYRcCJSwrQ"
    "XUt+Rc4uPv2D7OeQAT5mJfHNtI3ICW8QAommDQMjLyigHQdJpIlUCioa8NZWwxFJIjR4KW"
    "MUK+wBUDuFg4nEwlYRS0DBr4vhIyR0hOqJeIAkpuAwwl87AcYw5axrfvFQMQ6uJ7LOLX6Q"
    "0cEey7mTCJq8bWcihnUy3rUflOG6rRhtBhfjChifF0JseMLqwJlUrqYYo5klh9XvJAha+i"
    "i2YZzyiMNDEJQ0z5uHiEAl+mpjuEiQxA2B/Y8KprQwhKAHIYVXAJlYrGA/BUCK/Nk3qj3q"
    "yd1psVA+gwF5LGPBw6ARM6ajx9G8y1HkkUWmjGCVSHY0UCIrkM9y2SWJIJLiac9cyRdiPX"
    "4/ghzz2mvA58LEjIJ6vtKdBzjNwB9WdRytdwtnsX3Su7ffFJDTcR4tbX/Np2V2lMLZ3lpE"
    "enr5ScceSEu2vxEeNLzz431KtxPeh3NV4mpMf1iImdfQ1UTCiQDFJ2B5GbWp2xNKY2r6S2"
    "UjB1t8x61vMl67uS9ZhRKu1R9EnWXezj7bKe9fwHWY8W6a4kfX+TXLC3BeawqFZ2iLeyXK"
    "acHq+Zu5/PqGq+Mc1arWFWa6dNq95oWM3qonwuq9bV0U7vvSqlmZzGtTUhr65HheTPxogX"
    "c0+55LgLyffx9Jyge+hj6skxaBk1cw3Tz+3Ls/P25VHNzG2WfqQxtSqLeER8rJ9LME77HC"
    "Bk07I2oGxa1krMWrfMOaRUEvTC6RBJVzcBXV3NuVqIWZBfuNxpnXHb6rzeOdDPcmALFnAH"
    "Qzb8gR1ZZqUvOR7gareqmyx3q7p6vWtdrkQyiXzI2Z0ot+Kzfi9XlK2vKJpjyLUgBY/wT/"
    "kdUAr+sreSOk4kkoEodY4sPJ7uAIkbN2CProCqJziKeoKLJuEQOTd3iLtwScNMtsp2WTUx"
    "J3kJosjT9NQMVfxRh7SNOXHGRb3TSLO2e4oSm5f+6aH0T39iLlRIJTZ9yuUArw3/5XdEba"
    "oShCPzA6R7stGl7GTNpUzrsnQdRiUOt3aW8IerQX9F8z9xyXcDiSON34ZPxD7+h8xXw1Uw"
    "Mj3AmOnRRftrHvfZx0En39xTH+g8dzGb/wHJgt7t"
)
