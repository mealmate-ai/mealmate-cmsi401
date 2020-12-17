"""empty message

Revision ID: 0f7ce1ed9fe2
Revises: 55e1508decc2
Create Date: 2020-12-04 11:41:02.681098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f7ce1ed9fe2'
down_revision = '55e1508decc2'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('meal_log', 'log_id', nullable=False, autoincrement=True)


def downgrade():
    pass
