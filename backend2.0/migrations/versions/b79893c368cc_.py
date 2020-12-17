"""empty message

Revision ID: b79893c368cc
Revises: ed5cc352a4ef
Create Date: 2020-12-07 14:36:46.364058

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b79893c368cc'
down_revision = 'ed5cc352a4ef'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(
        op.f('ix_total_nutrition_food_desc'),
        'total_nutrition',
        [sa.text('to_tsvector(\'english\'::regconfig, "food_desc")')],
        postgresql_using='gin',
    )


def downgrade():
    op.drop_index(op.f('ix_total_nutrition_food_desc'), table_name='total_nutrition')
