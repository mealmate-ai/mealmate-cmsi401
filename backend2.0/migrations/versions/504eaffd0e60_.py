"""empty message

Revision ID: 504eaffd0e60
Revises: 1096f777d330
Create Date: 2021-04-16 11:47:43.834026

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '504eaffd0e60'
down_revision = '1096f777d330'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_logout', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('account', 'last_logout')
