def linearSearchProduct(productList, target_product):
  indices = []

  for index, product in enumerate(productList):
    if product == target_product:
       indices.append(index)

  return indices

products = ["shoes", "boot", "loafer", "shoes", "sandals", "shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
