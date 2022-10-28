function filter_list(l) {
  return l.filter(char => char.constructor.name.toLowerCase() != "string");
}
