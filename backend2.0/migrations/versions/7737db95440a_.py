"""empty message

Revision ID: 7737db95440a
Revises: b79893c368cc
Create Date: 2021-02-04 19:13:55.557913

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7737db95440a'
down_revision = 'b79893c368cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('password', sa.String(length=256)))


def downgrade():
    op.drop_column('account', 'password')
