"""initial migration

Revision ID: 30ccb3e20ee2
Revises: None
Create Date: 2014-12-14 15:39:23.914035

"""

# revision identifiers, used by Alembic.
revision = '30ccb3e20ee2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes',
    sa.Column('route_id', sa.String(length=50), nullable=False),
    sa.Column('agency_id', sa.String(length=50), nullable=True),
    sa.Column('route_short_name', sa.String(length=50), nullable=True),
    sa.Column('route_long_name', sa.String(length=150), nullable=True),
    sa.Column('route_desc', sa.String(length=150), nullable=True),
    sa.Column('route_type', sa.String(length=50), nullable=True),
    sa.Column('route_color', sa.String(length=50), nullable=True),
    sa.Column('route_text_color', sa.String(length=50), nullable=True),
    sa.Column('active', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('route_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routes')
    ### end Alembic commands ###
