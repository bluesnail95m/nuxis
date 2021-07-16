var alt = require('../alt');

class CategoryActions {
  update(categories) {
    this.dispatch(categories);
  }

  fetch() {
    this.dispatch();
  }

  failed(errorMessage) {
    this.dispatch(errorMessage);
  }
  
  clicked(category) {
      this.dispatch(category);
  }
}

var action = alt.createActions(CategoryActions);

module.exports = action;
exports.default = action;