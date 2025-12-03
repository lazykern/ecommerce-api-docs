Available market:US&UK
## What is a shipping template?
For 'Shipped by seller', TikTok requires at least one shipping template that includes the shipping rate displayed to the buyer.
Pain point:

* Seller may have no chance to know this information or set shipping template without logging to Seller center.
* The high failure rate of API listing products is mainly caused by not setting shipping templates

For those sellers, this widget can provide a shipping template(Prerequisite for listing products) for Seller
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/6bbfd92dc93648718faeaf9c3bfd5661~tplv-10qhjjqwgv-image.image" width="2698px" /></div>

## Showcase
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/20d5cee29de241d484ababf247918e18~tplv-10qhjjqwgv-image.image)
# Integration demo
## React framework
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
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/logistics:shippingTemplate
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/logistics:shippingTemplate']}>
      <RemoteWidget
        name={'@tiktokshop-widget/logistics:shippingTemplate'}
        className={'containerClass'}
        options={{
            onResult: (data: { code: number }) => {
              if (data.code === 0) {
                //Callback function for successful shipping template submission
              }
            },
            type: 'management',
        }} //Pass in the props required by the widget. If there are none, you don't need to pass them in.
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

const name = '@tiktokshop-widget/logistics:shippingTemplate';
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
      view?.render({
          onResult: (data: { code: number }) => {
              if (data.code === 0) {
                //Callback function for successful shipping template submission
              }
            },
            type: 'management',
      });
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
| 2024/2/22 | The first version is launched, providing basic functions of adding shipping templates. |
# Widget SDK User Guide
[Widget SDK User Guide](widget-sdk-user-guide)