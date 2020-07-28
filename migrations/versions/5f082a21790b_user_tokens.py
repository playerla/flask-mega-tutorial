"""user tokens

Revision ID: 5f082a21790b
Revises: e57560f6e507
Create Date: 2020-07-25 15:45:09.754319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f082a21790b'
down_revision = 'e57560f6e507'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification', 'timestamp',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    op.alter_column('notification', 'timestamp',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=True)
    # ### end Alembic commands ###
