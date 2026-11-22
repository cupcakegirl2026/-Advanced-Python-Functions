items=['pen','glue','sharpener','notebook','eraser']
stock_count=[1000,1000,1000,1000,1000]

inventory={item:count for item,count in zip (items,stock_count)}
print(f"full inventory: {inventory}")
