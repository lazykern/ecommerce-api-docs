Available market: US&UK
# What is Product optimizer Widget?
Product Optimizer leverages AI-powered recommendations to produce high-quality product information to sellers, including product names, descriptions, and images.
*Read on to learn more or check out Product Optimizer on TTS for reference [here](https://seller-us.tiktok.com/product/optimizer).
# What are the benefits of Product optimizer?
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c1d6d3d70e0a470aaef9fb78763a5cc8~tplv-10qhjjqwgv-image.image)
**Workflow**
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/a78f61a714ac444eb0b98b69635076f7~tplv-10qhjjqwgv-image.image)
# Showcase
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/0edbeaf819ad4850a3efb1ccf35bbb86~tplv-10qhjjqwgv-image.image)
# Integration demo
## React framework
Configure preload in `WidgetConfigProvider` preloadWidgetNames, you can put `WidgetConfigProvider` to the outermost preload time
```JSON
import { WidgetConfigProvider,RemoteWidget } from '@tiktokshop/widget-kit-react';

const getWidgetToken = async () => {
  const res: any = await get('https://xxx/api/v1/widget/access_token', {
    outer_shop_id: 'xxx',
    partner_type: '1',
  });
  if (res?.code === 0) {
    return res?.data;
  }
  return {};
};

const initOptions = {
  config: {
    shopId: 'xxx', //seller id, such as 123456
    oecRegion: 'xxx', //country,such as US
    appKey: 'xxx', //The key corresponding to the merchant's creation service
    isvInfo: {
      name: 'xxx', //ISV name,such as OPEN_PLATFORM
    },
  },
  getToken: getWidgetToken, //get auth token
  remotes: [
    {
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/product:optimizer
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/product:optimizer']}>
      <RemoteWidget
        name={'@tiktokshop-widget/product:optimizer'}
        className={'containerClass'}
        options={{}} //Pass in the props required by the widget. If there are none, you don't need to pass them in.
      />
    </WidgetConfigProvider>
  );
};
```

## Native js
```JSON
import React, { useEffect } from 'react';
import { get } from './utils/fetch';
import { loadWidget, init, WidgetComponent } from '@tiktokshop/widget-kit';

const name = '@tiktokshop-widget/product:optimizer';
let view = null;
export default () => {
  const getWidgetToken = async () => {
    const res: any = await get('https://xxx/api/v1/widget/access_token', {
      outer_shop_id: 'xxx',
      partner_type: '1',
    });
    if (res?.code === 0) {
      return res?.data;
    }
    return {};
  };

  const initWidget = () => {//It is recommended to initialize the widget in the outer layer and execute the preloadWidget([name]) method to preload resources.
    init({
      config: {
        shopId: 'xxx',
        oecRegion: 'US',
        appKey: 'xxx',
        isvInfo: {
          name: 'OPEN_PLATFORM',
        },
      },
      remotes: [
        {
          name,
        },
      ],
      getToken: getWidgetToken,
    });
  };
  useEffect(() => {
    initWidget();
    loadWidget(name).then((component: WidgetComponent) => {
      view = component.create(
        document.getElementById('widget-preview-container')!,
      );
      view?.render({});
    });
    return () => {
      view?.unmount();
    };
  }, []);
  return (
    <div
      className="widget-preview-container"
      id="widget-preview-container"></div>
  );
};
```

## Integration guide
[Widget SDK User Guide](widget-sdk-user-guide)
**Tips:**

* **Provide a notification for the seller to use the product optimizer**

It's recommended to provide the capability to remind sellers to optimize their product information after syncing products. This can be done by displaying a banner/toast on the product syncing page, reminding them to improve their product details.

* **General warning informing the seller to turn off product sync by specific API fields**

A general warning can be provided to inform sellers to turn off product information(eg product title, description, image) syncing to TTS in their connector app. By doing that, any edits made to a product in a DTC platform will not be synced to TTS once this is set by the seller.

* **Enables seller to turn off the product field synchronization(eg.title, description,image)**

it is recommended for ALL connector apps to add advanced settings to allow sellers to turn off product sync by different product fields. i.e., allow sellers to turn off sync for image, description, video, and title from a DTC platform to TTS. This way, sellers can edit information in a DTC platform for other sales channels without overriding information for TTS products (as these will be optimized by a PDP optimization tool).