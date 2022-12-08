"""empty message

Revision ID: e69d2d74e5d7
Revises: 283a7ab88f6f
Create Date: 2022-12-01 17:03:15.889260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e69d2d74e5d7'
down_revision = '283a7ab88f6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('climate', table_name='planets')
    op.drop_index('climate_2', table_name='planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('climate_2', 'planets', ['climate'], unique=False)
    op.create_index('climate', 'planets', ['climate'], unique=False)
    # ### end Alembic commands ###
