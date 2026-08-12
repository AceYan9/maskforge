from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "maskrule" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "deleted_at" TIMESTAMPTZ,
    "task_id" VARCHAR(32) NOT NULL UNIQUE,
    "rules" JSONB NOT NULL
);
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_task_task_id_6ec5cd" ON "task" ("task_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "task" DROP CONSTRAINT IF EXISTS "task_task_id_key";
        DROP INDEX IF EXISTS "uid_task_task_id_6ec5cd";
        DROP TABLE IF EXISTS "maskrule";"""


MODELS_STATE = (
    "eJztmW1v2jAQgP9K5E+dxCoaoDC+0a5bmQZMbbRNnSbLJAYyEpvaztqu479Pdt5foIR1LW"
    "X5ltz54stzPt/FuQcutbDDDweIzy88B4Oudg8IcuVFTlfTAFosYo0UCDRWVsBFfM7CUWMu"
    "GDIF6GoT5HBc04CFucnshbApAV2NeI4jhdTkgtlkGos8Yl97GAo6xWKGGehq377XNGATC9"
    "9iHt4u5nBiY8dKuWtbcm4lh+JuoWR9It6pgXK2MTSp47kkHry4EzNKotE2EVI6xQQzJLB8"
    "vGCedF96F7xp+Ea+p/EQ38WEjYUnyHNE4nXHMJYBCIcjA16eGRCCEoBMSiRcmwhJ4x5MpQ"
    "uv9aNmu9lpHDc7NQ0oNyNJe+lPHYPxDRWeoQGWSo8E8kcoxjFUk2FJAiKRh/sWCSxsFxcT"
    "TltmSFuB6WF4keUeUl4HPhTE5OPV9hToGUbWiDh3QcjXcDb6g7NLozf4JKdzOb92FL+ecS"
    "Y1upLeZaQHx6+knDJk+hkWPUT70jfONXmrXY2GZwov5WLK1IzxOOMKSJ+QJygk9AYiK7E6"
    "Q2lIbVlLpJK3sLaMetqyivquRD1klAh74H0cdQs7eLuopy0fIerBIt2VoL/cIOdzWyA+h0"
    "W18nSGWHF4EyaZ2HLBtsnh5y2ZLrqFDiZTMQNdraGvCe7n3sXpee/ioKFnAjYMNLpSLVOA"
    "ZRfE83g/XI6GxXgjg2zi2KbQfmuOzcUL3CjXYJUoUukS4jwY9L5mSZ9+HJ1k80A+4AQsl7"
    "IXnAS9YNQcjpE5v0HMgjkN1emqsXmVq7tZCSJoqkDKN5bvF3TIBuLzos5Zydd2zTKzqo65"
    "6pirjnmHy2rVMf+PUa865qpjDnKbY1bYMZ/Y05XlMmH0cM3c/XgGVfONrjcabb3eOO60mu"
    "12q1OPymdeta6OnvTfy1KaimlYW6tvlSf7VpnYDlbXJQgnbR4H8XOv7RRkvdXagLLeaq3E"
    "rHR5zj6lkqAjo30kXd8EdH0153ohZm7/wuX26pTZVrv1zoF+lu2aU4+ZGNLxD2yKMis9Z7"
    "iHq71V32S5t+qr17vSZQokFciBjN7wcis+bVc1KFs3KIqjz7UgBA/wT9jtUQj+8mQlsZ0I"
    "JDxeah+JLJ5uAwmPbcALagF35Ny0h5ltzopOTgPN2rNTFI+pTk/35fT0J2ZculQi6RMme9"
    "g2/JPPEZlUJQgHw/eQ7tFGTdnRmqZM6dJ0TUoE9lN701+ACZPqJ+DgBf0EXP4BVstzCw=="
)
