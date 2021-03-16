"""empty message

Revision ID: d21b591ba5a8
Revises: 7737db95440a
Create Date: 2021-03-16 01:07:51.361000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd21b591ba5a8'
down_revision = '7737db95440a'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('account', 'password',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)


def downgrade():
    op.alter_column('account', 'password',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)

