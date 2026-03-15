class MyListApp extends HTMLElement {
  set hass(hass) {
    if (!this._initialized) {
      this._initialized = true;
      const card = document.createElement('div');
      card.style.cssText = 'width:100%;height:100%;overflow:hidden;border-radius:12px;';
      const iframe = document.createElement('iframe');
      iframe.src = '/local/community/mylistapp-homeassistant/index.html';
      iframe.style.cssText = 'width:100%;height:600px;border:none;border-radius:12px;';
      iframe.allow = 'camera;geolocation';
      card.appendChild(iframe);
      this.appendChild(card);
    }
  }

  setConfig(config) {
    this._config = config;
    if (config.height) {
      const iframe = this.querySelector('iframe');
      if (iframe) iframe.style.height = config.height;
    }
  }

  getCardSize() {
    return 8;
  }

  static getStubConfig() {
    return { height: '600px' };
  }
}

customElements.define('mylistapp-homeassistant', MyListApp);

window.customCards = window.customCards || [];
window.customCards.push({
  type: 'mylistapp-homeassistant',
  name: 'My Lists',
  description: 'Personal checklist and mileage tracking app with AI photo recognition',
  preview: false
});

console.info('%c MY-LISTS-APP %c v1.0.0 ', 'color:white;background:#4CAF50;font-weight:bold;', 'color:#4CAF50;background:white;font-weight:bold;');
