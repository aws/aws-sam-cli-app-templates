import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import GetItems from '../src/components/GetItems.vue'

describe('GetItems', () => {    

    it('has proper input fileds', () => {
        const wrapper = mount(GetItems)
        
        const button = wrapper.find('button')        
        expect(button.exists()).toBe(true)        
    })

    it('accepts input values', () => {
        const wrapper = mount(GetItems)     

        // const button = wrapper.find('button')
        // button.trigger('click')
    })
})