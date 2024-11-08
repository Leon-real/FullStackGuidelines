# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Directory Tree
```
    frontend/               
    │
    ├── public/             
    │   └── index.html      # 애플리케이션 진입점 Vue 앱이 마운트되는 곳
    │
    └── src/
        ├── assets/         # 이미지, 폰트 등 정적 파일을 저장하는 폴더
        ├── components/     # 재사용 가능한 Vue컴포넌트들을 저장하는 폴더
        ├── router/         # Vue Router 설정 파일을 포함하는 폴더
        ├── views/          # 페이지 단위의 Vue 컴포넌트들을 저장하는 폴더
        ├── App.vue         # 루트 Vue 컴포넌트
        └── main.js         # Vue 애플리케이션을 초기화하고 필요한 플러그인을 등록하는 파일
```

### Guidelines
1. 새로운 페이지 추가하기
    1. `src/views/`폴더에 새 `.vuew`파일을 생성한다.
        ```
        <template>
        <div class="about">
            <h1>This is an about page</h1>
        </div>
        </template>

        <script>
        export default {
        name: 'AboutView'
        }
        </script>
        ```
    2. `src/router/index.js` 파일에 새 라우트를 추가한다
        ```
        import AboutView from '../views/AboutView.vue'

        const routes = [
        // ... 기존 라우트들
        {
            path: '/about',
            name: 'about',
            component: AboutView
        }
        ]
        ```
2. 새로운 컴포넌트 만들기
    1. `src/components/` 폴더에 새 `.vue` 파일을 생성한다
        ```
        <template>
            <button @click="handleClick">{{ text }}</button>
        </template>

        <script>
        export default {
        name: 'MyButton',
        props: {
            text: String
        },
        methods: {
            handleClick() {
            this.$emit('click')
            }
        }
        }
        </script>
        ```
    2. 다른 컴포넌트나 뷰에서 이 컴포넌트를 사용한다.
        ```
        <template>
            <div>
                <MyButton text="Click me" @click="doSomething" />
            </div>
        </template>

        <script>
        import MyButton from '@/components/MyButton.vue'

        export default {
        components: {
            MyButton
        },
        methods: {
            doSomething() {
            console.log('Button clicked!')
            }
        }
        }
        </script>
        ```
3. 라우터 네비게이션 추가하기
    1. `App.vue`파일에 네비게이션 링크를 추가한다.
        ```
        <template>
        <div id="app">
            <nav>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
            </nav>
            <router-view/>
        </div>
        </template>
        ```
4. 정적 자산을 사용하기
    1. 이미지 파일을 `src/assets/`폴더에 추가한다
    2. 컴포넌트에서 다음과 같이 사용한다.
        ```
        <template>
            <div>
                <img src="@/assets/logo.png" alt="Logo">
            </div>
        </template>
        ```