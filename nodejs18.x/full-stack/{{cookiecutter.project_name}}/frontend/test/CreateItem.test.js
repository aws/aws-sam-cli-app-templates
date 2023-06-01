import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import CreateItem from '../src/components/CreateItem.vue'

describe('CreateItem', () => {
    
    it('has proper input fileds', () => {
        const wrapper = mount(CreateItem)

        const userId = wrapper.find('#userId')
        expect(userId.element.id).toBe('userId')

        const userName = wrapper.find('#userName')
        expect(userName.element.id).toBe('userName')

        const button = wrapper.find('button')        
        expect(button.exists()).toBe(true)        
    })

    it('accepts input values', () => {
        const wrapper = mount(CreateItem)

        const userId = wrapper.find('#userId')
        userId.setValue('A123')

        const userName = wrapper.find('#userName')
        userName.setValue('John Doe')

        
        expect(userId.element.value).toBe('A123')
        expect(userName.element.value).toBe('John Doe')

        // const button = wrapper.find('button')
        // button.trigger('click')
    })
})