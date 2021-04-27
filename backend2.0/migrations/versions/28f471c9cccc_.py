"""empty message

Revision ID: 28f471c9cccc
Revises: 504eaffd0e60
Create Date: 2021-04-26 21:13:03.533223

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '28f471c9cccc'
down_revision = '504eaffd0e60'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('recipe', sa.Column('dish_type', sa.Text(), nullable=True))
    op.add_column('recipe', sa.Column('image', sa.Text(), nullable=True))
    op.drop_column('recipe', 'recipe_instructions')
    op.drop_column('recipe', 'recipe_ingredients')


def downgrade():
    op.add_column('recipe', sa.Column('recipe_ingredients', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('recipe', sa.Column('recipe_instructions', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('recipe', 'image')
    op.drop_column('recipe', 'dish_type')
