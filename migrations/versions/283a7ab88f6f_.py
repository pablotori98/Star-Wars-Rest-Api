"""empty message

Revision ID: 283a7ab88f6f
Revises: 496ade514967
Create Date: 2022-12-01 16:58:49.823385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283a7ab88f6f'
down_revision = '496ade514967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('planet_name'),
    sa.UniqueConstraint('planet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###