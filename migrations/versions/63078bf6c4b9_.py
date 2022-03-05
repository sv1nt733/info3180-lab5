"""empty message

Revision ID: 63078bf6c4b9
Revises: abf3c302cc4f
Create Date: 2022-03-05 15:44:52.954376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63078bf6c4b9'
down_revision = 'abf3c302cc4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
