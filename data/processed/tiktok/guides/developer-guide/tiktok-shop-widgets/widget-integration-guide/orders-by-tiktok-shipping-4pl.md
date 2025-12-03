Available market: US
# What is an Orders by TikTok Shipping(4PL) Widget?
**** Enable Seller in Shopify 1P and 3P Apps to process Orders by TikTok Shipping(4PL) orders and complete fulfillment.
*Read on to learn more or check out the Orders by TikTok Shipping(4PL) widget on TTS for reference [here](https://seller-us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=8706274700117762&from=feature_guide).
# Why do we build this?
Pinpoint**:** For sellers who use 3P to manage their orders, when it comes to Orders by TikTok Shipping(4PL) orders sellers need to carry out fulfillment actions in the TTS seller center, which breaks the workflow of sellers' operation in 1P/3P APP.
Solution: enables sellers to process Orders by TikTok Shipping(4PL) orders individually/in batches in the 3P APP.
# Workflow
Select orders in batches - > > create labels - > > print labels - > > process shipments
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/32be0a8919ff4f219135306cab6680b2~tplv-10qhjjqwgv-image.image)
# Showcase
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c26c6aaeb38e4c24bf0cd8b812c00b5d~tplv-10qhjjqwgv-image.image" width="1896px" /></div>

Tips:

* The Orders by TikTok Shipping(4PL) widget will only display Orders by TikTok Shipping(4PL) orders to the seller. It is advisable to use a clear tab name for sellers, such as "Manage Orders Fulfilled by TikTok" or "Manage TikTok Orders by TikTok Shipping(4PL) Orders."

# Integration demo
Configure preload in `WidgetConfigProvider` preloadWidgetNames, you can put `WidgetConfigProvider` to the outermost preload time
```TypeScript
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
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/order:manageOrders
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/order:manageOrders']}>
      <RemoteWidget
        name={'@tiktokshop-widget/order:manageOrders'}
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

const name = '@tiktokshop-widget/order:manageOrders';
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

# Change log
| Release date | Update |
| --- | --- |
| 2024/1/22 | The first version is launched, providing basic functions of 4PL. |
# Widget SDK User Guide
[Widget SDK User Guide](widget-sdk-user-guide)