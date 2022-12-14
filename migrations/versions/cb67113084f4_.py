"""empty message

Revision ID: cb67113084f4
Revises: 54d112f726ec
Create Date: 2022-12-05 16:21:06.105702

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb67113084f4'
down_revision = '54d112f726ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name'),
    sa.UniqueConstraint('planet_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tablefavourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tablefavouritesPeople',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('planet_name', table_name='tableplanets')
    op.drop_index('planet_name_2', table_name='tableplanets')
    op.drop_table('tableplanets')
    op.drop_index('email', table_name='tableuser')
    op.drop_index('email_2', table_name='tableuser')
    op.drop_table('tableuser')
    op.drop_index('name', table_name='tablepeople')
    op.drop_index('name_2', table_name='tablepeople')
    op.drop_table('tablepeople')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tablepeople',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('height', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gender', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('mass', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name_2', 'tablepeople', ['name'], unique=False)
    op.create_index('name', 'tablepeople', ['name'], unique=False)
    op.create_table('tableuser',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`is_active` in (0,1))', name='tableuser_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email_2', 'tableuser', ['email'], unique=False)
    op.create_index('email', 'tableuser', ['email'], unique=False)
    op.create_table('tableplanets',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('planet_name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('climate', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('rotation_period', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('orbital_period', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('planet_name_2', 'tableplanets', ['planet_name'], unique=False)
    op.create_index('planet_name', 'tableplanets', ['planet_name'], unique=False)
    op.drop_table('tablefavouritesPeople')
    op.drop_table('tablefavourites')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
