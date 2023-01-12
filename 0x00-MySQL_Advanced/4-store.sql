-- Create a trigger that decreases stock of an item after an order is sent

CREATE TRIGGER diff BEFORE INSERT ON `orders`
FOR EACH ROW UPDATE `items` SET quantity = quantity - NEW.number WHERE NEW.item_name = `items`.name;