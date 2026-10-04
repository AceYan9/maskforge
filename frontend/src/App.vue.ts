/* __placeholder__ */

const { defineProps, defineSlots, defineEmits, defineExpose, defineModel, defineOptions, withDefaults, } = await import('vue');
let __VLS_modelEmitsType!: {};

const __VLS_componentsOption = {};

let __VLS_name!: 'App';
function __VLS_template() {
let __VLS_ctx!: InstanceType<__VLS_PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {
};
/* Components */
let __VLS_otherComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C } ? C : {}> & typeof __VLS_componentsOption;
let __VLS_own!: __VLS_SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & (new () => { $slots: typeof __VLS_slots })>;
let __VLS_localComponents!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
let __VLS_components!: typeof __VLS_localComponents & __VLS_GlobalComponents & typeof __VLS_ctx;
/* Style Scoped */
type __VLS_StyleScopedClasses = {};
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_resolvedLocalAndGlobalComponents!: {}
& __VLS_WithComponent<'ElContainer', typeof __VLS_localComponents, "ElContainer", "elContainer", "el-container">
& __VLS_WithComponent<'ElAside', typeof __VLS_localComponents, "ElAside", "elAside", "el-aside">
& __VLS_WithComponent<'ElMain', typeof __VLS_localComponents, "ElMain", "elMain", "el-main">
& __VLS_WithComponent<'RouterView', typeof __VLS_localComponents, "RouterView", "routerView", "router-view">
;
__VLS_intrinsicElements.div;__VLS_intrinsicElements.div;
__VLS_components.ElContainer;__VLS_components.elContainer;__VLS_components.ElContainer;__VLS_components.elContainer;
// @ts-ignore
[ElContainer,ElContainer,];
__VLS_components.ElAside;__VLS_components.elAside;__VLS_components.ElAside;__VLS_components.elAside;__VLS_components.ElAside;__VLS_components.elAside;__VLS_components.ElAside;__VLS_components.elAside;
// @ts-ignore
[ElAside,ElAside,ElAside,ElAside,];
__VLS_components.ElMain;__VLS_components.elMain;__VLS_components.ElMain;__VLS_components.elMain;
// @ts-ignore
[ElMain,ElMain,];
__VLS_components.RouterView;__VLS_components.routerView;
// @ts-ignore
[RouterView,];
{
const __VLS_0 = __VLS_intrinsicElements["div"];
const __VLS_1 = __VLS_elementAsFunctionalComponent(__VLS_0);
const __VLS_2 = __VLS_1({ ...{ }, class: ("common-layout"), }, ...__VLS_functionalComponentArgsRest(__VLS_1));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_0, typeof __VLS_2> & Record<string, unknown>) => void)({ ...{ }, class: ("common-layout"), });
{
const __VLS_5 = ({} as 'ElContainer' extends keyof typeof __VLS_ctx ? { 'ElContainer': typeof __VLS_ctx.ElContainer }: 'elContainer' extends keyof typeof __VLS_ctx ? { 'ElContainer': typeof __VLS_ctx.elContainer }: 'el-container' extends keyof typeof __VLS_ctx ? { 'ElContainer': typeof __VLS_ctx["el-container"] }: typeof __VLS_resolvedLocalAndGlobalComponents).ElContainer;
const __VLS_6 = __VLS_asFunctionalComponent(__VLS_5, new __VLS_5({...{ }, }));
({} as { ElContainer: typeof __VLS_5 }).ElContainer;
({} as { ElContainer: typeof __VLS_5 }).ElContainer;
const __VLS_7 = __VLS_6({ ...{ }, }, ...__VLS_functionalComponentArgsRest(__VLS_6));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_5, typeof __VLS_7> & Record<string, unknown>) => void)({ ...{ }, });
{
const __VLS_10 = ({} as 'ElAside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx.ElAside }: 'elAside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx.elAside }: 'el-aside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx["el-aside"] }: typeof __VLS_resolvedLocalAndGlobalComponents).ElAside;
const __VLS_11 = __VLS_asFunctionalComponent(__VLS_10, new __VLS_10({...{ }, width: ("20%"), }));
({} as { ElAside: typeof __VLS_10 }).ElAside;
({} as { ElAside: typeof __VLS_10 }).ElAside;
const __VLS_12 = __VLS_11({ ...{ }, width: ("20%"), }, ...__VLS_functionalComponentArgsRest(__VLS_11));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_10, typeof __VLS_12> & Record<string, unknown>) => void)({ ...{ }, width: ("20%"), });
const __VLS_13 = __VLS_pickFunctionalComponentCtx(__VLS_10, __VLS_12)!;
}
{
const __VLS_15 = ({} as 'ElMain' extends keyof typeof __VLS_ctx ? { 'ElMain': typeof __VLS_ctx.ElMain }: 'elMain' extends keyof typeof __VLS_ctx ? { 'ElMain': typeof __VLS_ctx.elMain }: 'el-main' extends keyof typeof __VLS_ctx ? { 'ElMain': typeof __VLS_ctx["el-main"] }: typeof __VLS_resolvedLocalAndGlobalComponents).ElMain;
const __VLS_16 = __VLS_asFunctionalComponent(__VLS_15, new __VLS_15({...{ }, }));
({} as { ElMain: typeof __VLS_15 }).ElMain;
({} as { ElMain: typeof __VLS_15 }).ElMain;
const __VLS_17 = __VLS_16({ ...{ }, }, ...__VLS_functionalComponentArgsRest(__VLS_16));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_15, typeof __VLS_17> & Record<string, unknown>) => void)({ ...{ }, });
{
const __VLS_20 = ({} as 'RouterView' extends keyof typeof __VLS_ctx ? { 'RouterView': typeof __VLS_ctx.RouterView }: 'routerView' extends keyof typeof __VLS_ctx ? { 'RouterView': typeof __VLS_ctx.routerView }: 'router-view' extends keyof typeof __VLS_ctx ? { 'RouterView': typeof __VLS_ctx["router-view"] }: typeof __VLS_resolvedLocalAndGlobalComponents).RouterView;
const __VLS_21 = __VLS_asFunctionalComponent(__VLS_20, new __VLS_20({...{ }, }));
({} as { RouterView: typeof __VLS_20 }).RouterView;
const __VLS_22 = __VLS_21({ ...{ }, }, ...__VLS_functionalComponentArgsRest(__VLS_21));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_20, typeof __VLS_22> & Record<string, unknown>) => void)({ ...{ }, });
const __VLS_23 = __VLS_pickFunctionalComponentCtx(__VLS_20, __VLS_22)!;
}
(__VLS_18.slots!).default;
const __VLS_18 = __VLS_pickFunctionalComponentCtx(__VLS_15, __VLS_17)!;
}
{
const __VLS_25 = ({} as 'ElAside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx.ElAside }: 'elAside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx.elAside }: 'el-aside' extends keyof typeof __VLS_ctx ? { 'ElAside': typeof __VLS_ctx["el-aside"] }: typeof __VLS_resolvedLocalAndGlobalComponents).ElAside;
const __VLS_26 = __VLS_asFunctionalComponent(__VLS_25, new __VLS_25({...{ }, width: ("20%"), }));
({} as { ElAside: typeof __VLS_25 }).ElAside;
({} as { ElAside: typeof __VLS_25 }).ElAside;
const __VLS_27 = __VLS_26({ ...{ }, width: ("20%"), }, ...__VLS_functionalComponentArgsRest(__VLS_26));
({} as (props: __VLS_FunctionalComponentProps<typeof __VLS_25, typeof __VLS_27> & Record<string, unknown>) => void)({ ...{ }, width: ("20%"), });
const __VLS_28 = __VLS_pickFunctionalComponentCtx(__VLS_25, __VLS_27)!;
}
(__VLS_8.slots!).default;
const __VLS_8 = __VLS_pickFunctionalComponentCtx(__VLS_5, __VLS_7)!;
}
(__VLS_3.slots!).default;
const __VLS_3 = __VLS_pickFunctionalComponentCtx(__VLS_0, __VLS_2)!;
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
}
var __VLS_slots!:{
};
return __VLS_slots;
}
const __VLS_internalComponent = (await import('vue')).defineComponent({
setup() {
return {
};
},
});
export default (await import('vue')).defineComponent({
setup() {
return {
};
},
});

; declare global {
// @ts-ignore
type __VLS_IntrinsicElements = __VLS_PickNotAny<import('vue/jsx-runtime').JSX.IntrinsicElements, __VLS_PickNotAny<JSX.IntrinsicElements, Record<string, any>>>;
// @ts-ignore
type __VLS_Element = __VLS_PickNotAny<import('vue/jsx-runtime').JSX.Element, JSX.Element>;
// @ts-ignore
type __VLS_GlobalComponents = __VLS_PickNotAny<import('vue').GlobalComponents, {}> & __VLS_PickNotAny<import('@vue/runtime-core').GlobalComponents, {}> & __VLS_PickNotAny<import('@vue/runtime-dom').GlobalComponents, {}> & Pick<typeof import('vue'), 'Transition' | 'TransitionGroup' | 'KeepAlive' | 'Suspense' | 'Teleport'>;
type __VLS_IsAny<T> = 0 extends 1 & T ? true : false;
type __VLS_PickNotAny<A, B> = __VLS_IsAny<A> extends true ? B : A;

const __VLS_intrinsicElements: __VLS_IntrinsicElements;

// v-for
function __VLS_getVForSourceType(source: number): [number, number, number][];
function __VLS_getVForSourceType(source: string): [string, number, number][];
function __VLS_getVForSourceType<T extends any[]>(source: T): [
	item: T[number],
	key: number,
	index: number,
][];
function __VLS_getVForSourceType<T extends { [Symbol.iterator](): Iterator<any> }>(source: T): [
	item: T extends { [Symbol.iterator](): Iterator<infer T1> } ? T1 : never, 
	key: number,
	index: undefined,
][];
// #3845
function __VLS_getVForSourceType<T extends number | { [Symbol.iterator](): Iterator<any> }>(source: T): [
	item: number | (Exclude<T, number> extends { [Symbol.iterator](): Iterator<infer T1> } ? T1 : never), 
	key: number,
	index: undefined,
][];
function __VLS_getVForSourceType<T>(source: T): [
	item: T[keyof T],
	key: keyof T,
	index: number,
][];

// @ts-ignore
function __VLS_getSlotParams<T>(slot: T): Parameters<__VLS_PickNotAny<NonNullable<T>, (...args: any[]) => any>>;
// @ts-ignore
function __VLS_getSlotParam<T>(slot: T): Parameters<__VLS_PickNotAny<NonNullable<T>, (...args: any[]) => any>>[0];
function __VLS_directiveFunction<T>(dir: T):
	T extends import('vue').ObjectDirective<infer E, infer V> | import('vue').FunctionDirective<infer E, infer V> ? (value: V) => void
	: T;
function __VLS_withScope<T, K>(ctx: T, scope: K): ctx is T & K;
function __VLS_makeOptional<T>(t: T): { [K in keyof T]?: T[K] };

type __VLS_SelfComponent<N, C> = string extends N ? {} : N extends string ? { [P in N]: C } : {};
type __VLS_WithComponent<N0 extends string, LocalComponents, N1 extends string, N2 extends string, N3 extends string> =
	N1 extends keyof LocalComponents ? N1 extends N0 ? Pick<LocalComponents, N0 extends keyof LocalComponents ? N0 : never> : { [K in N0]: LocalComponents[N1] } :
	N2 extends keyof LocalComponents ? N2 extends N0 ? Pick<LocalComponents, N0 extends keyof LocalComponents ? N0 : never> : { [K in N0]: LocalComponents[N2] } :
	N3 extends keyof LocalComponents ? N3 extends N0 ? Pick<LocalComponents, N0 extends keyof LocalComponents ? N0 : never> : { [K in N0]: LocalComponents[N3] } :
	N1 extends keyof __VLS_GlobalComponents ? N1 extends N0 ? Pick<__VLS_GlobalComponents, N0 extends keyof __VLS_GlobalComponents ? N0 : never> : { [K in N0]: __VLS_GlobalComponents[N1] } :
	N2 extends keyof __VLS_GlobalComponents ? N2 extends N0 ? Pick<__VLS_GlobalComponents, N0 extends keyof __VLS_GlobalComponents ? N0 : never> : { [K in N0]: __VLS_GlobalComponents[N2] } :
	N3 extends keyof __VLS_GlobalComponents ? N3 extends N0 ? Pick<__VLS_GlobalComponents, N0 extends keyof __VLS_GlobalComponents ? N0 : never> : { [K in N0]: __VLS_GlobalComponents[N3] } :
	{ [K in N0]: unknown }

type __VLS_FillingEventArg_ParametersLength<E extends (...args: any) => any> = __VLS_IsAny<Parameters<E>> extends true ? -1 : Parameters<E>['length'];
type __VLS_FillingEventArg<E> = E extends (...args: any) => any ? __VLS_FillingEventArg_ParametersLength<E> extends 0 ? ($event?: undefined) => ReturnType<E> : E : E;
function __VLS_asFunctionalComponent<T, K = T extends new (...args: any) => any ? InstanceType<T> : unknown>(t: T, instance?: K):
	T extends new (...args: any) => any
	? (props: (K extends { $props: infer Props } ? Props : any) & Record<string, unknown>, ctx?: any) => __VLS_Element & { __ctx?: {
		attrs?: any,
		slots?: K extends { $slots: infer Slots } ? Slots : any,
		emit?: K extends { $emit: infer Emit } ? Emit : any
	} & { props?: (K extends { $props: infer Props } ? Props : any) & Record<string, unknown>; expose?(exposed: K): void; } }
	: T extends () => any ? (props: {}, ctx?: any) => ReturnType<T>
	: T extends (...args: any) => any ? T
	: (_: {} & Record<string, unknown>, ctx?: any) => { __ctx?: { attrs?: any, expose?: any, slots?: any, emit?: any, props?: {} & Record<string, unknown> } };
function __VLS_elementAsFunctionalComponent<T>(t: T): (_: T & Record<string, unknown>, ctx?: any) => { __ctx?: { attrs?: any, expose?: any, slots?: any, emit?: any, props?: T & Record<string, unknown> } };
function __VLS_functionalComponentArgsRest<T extends (...args: any) => any>(t: T): Parameters<T>['length'] extends 2 ? [any] : [];
function __VLS_pickEvent<E1, E2>(emitEvent: E1, propEvent: E2): __VLS_FillingEventArg<
	__VLS_PickNotAny<
		__VLS_AsFunctionOrAny<E2>,
		__VLS_AsFunctionOrAny<E1>
	>
> | undefined;
function __VLS_pickFunctionalComponentCtx<T, K>(comp: T, compInstance: K): __VLS_PickNotAny<
	'__ctx' extends keyof __VLS_PickNotAny<K, {}> ? K extends { __ctx?: infer Ctx } ? Ctx : never : any
	, T extends (props: any, ctx: infer Ctx) => any ? Ctx : any
>;
type __VLS_FunctionalComponentProps<T, K> =
	'__ctx' extends keyof __VLS_PickNotAny<K, {}> ? K extends { __ctx?: { props?: infer P } } ? NonNullable<P> : never
	: T extends (props: infer P, ...args: any) => any ? P :
	{};
type __VLS_AsFunctionOrAny<F> = unknown extends F ? any : ((...args: any) => any) extends F ? F : any;

function __VLS_normalizeSlot<S>(s: S): S extends () => infer R ? (props: {}) => R : S;

/**
 * emit
 */
// fix https://github.com/vuejs/language-tools/issues/926
type __VLS_UnionToIntersection<U> = (U extends unknown ? (arg: U) => unknown : never) extends ((arg: infer P) => unknown) ? P : never;
type __VLS_OverloadUnionInner<T, U = unknown> = U & T extends (...args: infer A) => infer R
	? U extends T
	? never
	: __VLS_OverloadUnionInner<T, Pick<T, keyof T> & U & ((...args: A) => R)> | ((...args: A) => R)
	: never;
type __VLS_OverloadUnion<T> = Exclude<
	__VLS_OverloadUnionInner<(() => never) & T>,
	T extends () => never ? never : () => never
>;
type __VLS_ConstructorOverloads<T> = __VLS_OverloadUnion<T> extends infer F
	? F extends (event: infer E, ...args: infer A) => any
	? { [K in E & string]: (...args: A) => void; }
	: never
	: never;
type __VLS_NormalizeEmits<T> = __VLS_PrettifyGlobal<
	__VLS_UnionToIntersection<
		__VLS_ConstructorOverloads<T> & {
			[K in keyof T]: T[K] extends any[] ? { (...args: T[K]): void } : never
		}
	>
>;
type __VLS_PrettifyGlobal<T> = { [K in keyof T]: T[K]; } & {};
}

type __VLS_IntrinsicElementsCompletion = __VLS_IntrinsicElements;
