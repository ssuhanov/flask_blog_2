"""empty message

Revision ID: caaad1928f4f
Revises: de1d74364f4a
Create Date: 2020-05-25 20:41:31.419887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caaad1928f4f'
down_revision = 'de1d74364f4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
