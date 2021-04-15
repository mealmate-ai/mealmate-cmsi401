"""empty message

Revision ID: 08c0da289311
Revises: d21b591ba5a8
Create Date: 2021-04-15 15:45:56.474631

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '08c0da289311'
down_revision = 'd21b591ba5a8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('goal', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('account', 'goal')
