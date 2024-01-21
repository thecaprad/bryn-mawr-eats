export const useUtils = () => {
  const prettyQuantity = (quantity) => {
    if (Math.round(quantity) !== quantity) {
      return quantity.toFixed(2);
    }
    return quantity;
  };

  return {
    prettyQuantity,
  };
};
