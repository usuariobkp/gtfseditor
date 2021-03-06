"""create agency tags table

Revision ID: 8d37ec247e2
Revises: 1ccf9b9d7a90
Create Date: 2015-10-30 11:33:01.668518

"""

# revision identifiers, used by Alembic.
revision = '8d37ec247e2'
down_revision = '1ccf9b9d7a90'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency_tags',
        sa.Column('agency_id', sa.Integer(), nullable=False),
        sa.Column('transaction_id', sa.Integer(), nullable=True),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['agency_id', 'transaction_id'], [u'agency_version.agency_id', u'agency_version.transaction_id'], ),
        sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
        sa.PrimaryKeyConstraint('agency_id', 'tag_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency_tags')
    ### end Alembic commands ###
