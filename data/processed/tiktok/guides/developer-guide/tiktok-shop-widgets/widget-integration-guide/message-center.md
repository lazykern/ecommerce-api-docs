# Introduction
The Message Center widget provides sellers with a centralized location to view all updates related to the TikTok Shop, including information on violations, appeals, policies, orders, products, and more
# Benefits

* Engage sellers connected through your to view important TikTok Shop messages
* Help the seller understand policy updates and actions taken by sellers


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
      name: 'xxx', //Integrated business name, provided by the open platform,such as:@tiktokshop-widget/message:inbox
    },
  ],
};

export default () => {
  return (
    <WidgetConfigProvider
      config={initOptions.config}
      getToken={initOptions.getToken}
      remotes={initOptions.remotes}
      preloadWidgetNames={['@tiktokshop-widget/message:inbox']}>
      <RemoteWidget
        name={'@tiktokshop-widget/message:inbox'}
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

const name = '@tiktokshop-widget/message:inbox';
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
| 2024/2/22 | The first version is launched, providing basic functions of managing seller center messages |
# Widget SDK User Guide
[Widget SDK User Guide](widget-sdk-user-guide)