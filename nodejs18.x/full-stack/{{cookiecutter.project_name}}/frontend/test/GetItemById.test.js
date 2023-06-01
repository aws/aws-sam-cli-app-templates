import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import GetItemById from '../src/components/GetItemById.vue'

describe('GetItemById', () => {

    it('has proper input fileds', () => {
        const wrapper = mount(GetItemById)

        const userId = wrapper.find('#userId')
        expect(userId.element.id).toBe('userId')

        const button = wrapper.find('button')        
        expect(button.exists()).toBe(true)        
    })

    it('accepts input values', () => {
        const wrapper = mount(GetItemById)

        const userId = wrapper.find('#userId')
        userId.setValue('A123')
        
        expect(userId.element.value).toBe('A123')        

        // const button = wrapper.find('button')
        // button.trigger('click')
    })
})