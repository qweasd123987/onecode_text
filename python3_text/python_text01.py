import random
import datetime

class Inventory:
    def __init__(self):
        # 模拟库存数据
        self.stock = {
            "iPhone15": 5,
            "ThinkPad_X1": 3,
            "PS5": 2,
            "Switch": 10
        }

    def check_stock(self, item, qty):
        if item not in self.stock:
            raise ValueError(f"商品 {item} 不存在")
        if self.stock[item] >= qty:
            return True
        return False

    def reduce_stock(self, item, qty):
        if self.check_stock(item, qty):
            self.stock[item] -= qty
        else:
            raise ValueError(f"库存不足: {item} 仅剩 {self.stock[item]} 件")


class User:
    def __init__(self, name, credit_score):
        self.name = name
        self.credit_score = credit_score  # 模拟信用分


class OrderSystem:
    def __init__(self, inventory):
        self.inventory = inventory
        self.log = []

    def apply_discount(self, user, price, coupon=None):
        discount = 0.0
        if coupon == "NEWUSER10":
            discount = 0.1
        elif coupon == "VIP20" and user.credit_score > 700:
            discount = 0.2
        elif user.credit_score < 400:
            # 信用过低，收取风险附加费
            discount = -0.15
        return price * (1 - discount)

    def create_order(self, user, item, qty, coupon=None):
        try:
            # Step 1: 检查库存
            if not self.inventory.check_stock(item, qty):
                return f"下单失败: 库存不足 ({item})"

            # Step 2: 基础价格计算
            base_price = random.randint(200, 2000) * qty

            # Step 3: 折扣计算
            final_price = self.apply_discount(user, base_price, coupon)

            # Step 4: 减少库存
            self.inventory.reduce_stock(item, qty)

            # Step 5: 生成订单号
            order_id = f"ORD{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100,999)}"

            # Step 6: 写日志
            order_info = {
                "order_id": order_id,
                "user": user.name,
                "item": item,
                "qty": qty,
                "final_price": round(final_price, 2),
                "timestamp": datetime.datetime.now().isoformat()
            }
            self.log.append(order_info)

            return f"下单成功: {order_info}"
        except Exception as e:
            return f"订单异常: {e}"

    def show_logs(self):
        for entry in self.log:
            print(entry)


if __name__ == "__main__":
    inv = Inventory()
    system = OrderSystem(inv)

    # 模拟用户
    u1 = User("Alice", 750)
    u2 = User("Bob", 350)

    # 下单测试
    print(system.create_order(u1, "iPhone15", 1, "VIP20"))
    print(system.create_order(u2, "PS5", 1))  # 信用差，有风险附加费
    print(system.create_order(u1, "ThinkPad_X1", 5))  # 超过库存

    print("\n--- 系统日志 ---")
    system.show_logs()
