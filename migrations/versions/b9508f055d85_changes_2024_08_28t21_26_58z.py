"""Changes 2024-08-28T21:26:58Z

Revision ID: b9508f055d85
Revises: 
Create Date: 2024-08-29 00:26:58.808587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9508f055d85'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('os_order',
    sa.Column('order_number', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_os_order_order_number'), 'os_order', ['order_number'], unique=True)
    op.create_table('os_serial_number',
    sa.Column('serial_number_code', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_os_serial_number_serial_number_code'), 'os_serial_number', ['serial_number_code'], unique=True)
    op.create_table('os_sku',
    sa.Column('sku_code', sa.Text(), nullable=False),
    sa.Column('sku_serial_number_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sku_serial_number_id'], ['os_serial_number.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_os_sku_sku_code'), 'os_sku', ['sku_code'], unique=True)
    op.create_table('os_sku_characteristics',
    sa.Column('sku_characteristics_sku_id', sa.Integer(), nullable=True),
    sa.Column('sku_characteristics_weight', sa.Float(), nullable=True),
    sa.Column('sku_characteristics_volume', sa.Float(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sku_characteristics_sku_id'], ['os_sku.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('os_sku_characteristics')
    op.drop_index(op.f('ix_os_sku_sku_code'), table_name='os_sku')
    op.drop_table('os_sku')
    op.drop_index(op.f('ix_os_serial_number_serial_number_code'), table_name='os_serial_number')
    op.drop_table('os_serial_number')
    op.drop_index(op.f('ix_os_order_order_number'), table_name='os_order')
    op.drop_table('os_order')
    # ### end Alembic commands ###
